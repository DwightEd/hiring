"""AI 模块数值用例与中心差分梯度检查；不依赖 PyTorch。"""
import importlib
import math
import unittest
from tests.support import catalog
try:
    import numpy as np
except ImportError:
    np = None


def numeric_gradient(function, x, eps=1e-6):
    x = x.copy()
    result = np.zeros_like(x)
    for index in np.ndindex(x.shape):
        previous = x[index]
        x[index] = previous + eps
        positive = function(x)
        x[index] = previous - eps
        negative = function(x)
        x[index] = previous
        result[index] = (positive - negative) / (2 * eps)
    return result


@unittest.skipIf(np is None,'AI 测试需要 pip install -r requirements.txt')
class AITests(unittest.TestCase):
    def ai(self,name):
        return importlib.import_module('ai.'+name)

    def close(self,a,b,atol=1e-7):
        np.testing.assert_allclose(a,b,atol=atol,rtol=1e-5)

    def test_catalog_coverage(self):
        ids={row['id'] for row in catalog('ai')}
        self.assertEqual(len(ids),36)
        self.assertTrue(all(hasattr(self,'test_'+identifier) for identifier in ids))

    def test_softmax(self):
        module=self.ai('softmax');x=np.array([[1000.,1001.,1002.],[-1.,0.,2.]])
        p=module.softmax(x);self.close(p.sum(-1),[1,1])
        self.close(p,module.softmax(x-999))
        g=np.arange(6.).reshape(2,3)
        self.close(module.backward(p,g),numeric_gradient(lambda z:(module.softmax(z)*g).sum(),x))

    def test_cross_entropy(self):
        module=self.ai('cross_entropy');x=np.array([[2.,-1.,0.],[1.,3.,-2.]])
        y=np.array([0,1]);loss,gradient=module.cross_entropy(x,y)
        self.assertGreater(loss,0)
        self.close(gradient,numeric_gradient(lambda z:module.cross_entropy(z,y)[0],x))
        loss,gradient=module.cross_entropy(np.array([[1000.,-1000.]]),np.array([1]))
        self.assertEqual(loss,2000);self.assertTrue(np.isfinite(gradient).all())

    def test_sigmoid_bce(self):
        module=self.ai('sigmoid_bce');x=np.array([-1000.,0.,1000.])
        self.close(module.sigmoid(x),[0,.5,1])
        x=np.array([-2.,.3,1.]);y=np.array([0.,1.,0.])
        loss,g=module.binary_cross_entropy(x,y)
        self.close(g,numeric_gradient(lambda z:module.binary_cross_entropy(z,y)[0],x))

    def test_layer_norm(self):
        module=self.ai('layer_norm');rng=np.random.default_rng(4)
        x=rng.normal(size=(2,3,4));gamma=rng.normal(size=4);beta=rng.normal(size=4);g=rng.normal(size=x.shape)
        output,cache=module.layer_norm(x,gamma,beta)
        dx,dgamma,dbeta=module.backward(g,cache)
        self.close(dx,numeric_gradient(lambda z:(module.layer_norm(z,gamma,beta)[0]*g).sum(),x))
        self.close(dgamma,numeric_gradient(lambda z:(module.layer_norm(x,z,beta)[0]*g).sum(),gamma))
        self.close(dbeta,numeric_gradient(lambda z:(module.layer_norm(x,gamma,z)[0]*g).sum(),beta))
        self.assertTrue(np.isfinite(module.layer_norm(np.ones((1,4)),gamma,beta)[0]).all())

    def test_rms_norm(self):
        x=np.array([[3.,4.],[0.,0.]])
        self.close(self.ai('rms_norm').rms_norm(x,np.ones(2)),x/np.sqrt((x*x).mean(-1,keepdims=True)+1e-6))

    def test_batch_norm(self):
        module=self.ai('batch_norm');bn=module.BatchNorm(2,momentum=.5)
        x=np.array([[1.,3.],[3.,7.]])
        y=bn(x);self.close(y.mean(0),[0,0])
        self.close(bn.mean,[1,2.5]);self.close(bn.variance,[1.5,4.5])
        before=bn.mean.copy();self.close(bn(x,False),(x-bn.mean)/np.sqrt(bn.variance+1e-5))
        self.close(bn.mean,before)
        with self.assertRaises(ValueError):bn(x[:1])

    def test_attention(self):
        module=self.ai('attention');rng=np.random.default_rng(7)
        q,k,v=rng.normal(size=(2,3)),rng.normal(size=(3,3)),rng.normal(size=(3,2))
        mask=np.array([[True,False,True],[False,False,False]])
        output,cache=module.attention(q,k,v,mask)
        self.close(output[1],[0,0]);self.assertTrue(np.isfinite(output).all())
        g=rng.normal(size=output.shape);dq,dk,dv=module.backward(g,cache)
        self.close(dq,numeric_gradient(lambda z:(module.attention(z,k,v,mask)[0]*g).sum(),q))
        self.close(dk,numeric_gradient(lambda z:(module.attention(q,z,v,mask)[0]*g).sum(),k))
        self.close(dv,numeric_gradient(lambda z:(module.attention(q,k,z,mask)[0]*g).sum(),v))

    def test_multihead_attention(self):
        rng=np.random.default_rng(10);x=rng.normal(size=(2,3,4));identity=np.eye(4)
        result=self.ai('multihead_attention').multihead_attention(x,identity,identity,identity,identity,2)
        expected=[]
        for head in range(2):
            part=x[...,head*2:head*2+2]
            expected.append(self.ai('attention').attention(part,part,part,np.tril(np.ones((3,3),bool)))[0])
        self.close(result,np.concatenate(expected,axis=-1))
        kv=identity[:,:2]
        result=self.ai('multihead_attention').multihead_attention(x,identity,kv,kv,identity,2,kv_heads=1)
        self.assertEqual(result.shape,x.shape)
        # 因果遮罩：更改未来 token 不应改变第一个位置。
        changed=x.copy();changed[:,1:]+=100
        result2=self.ai('multihead_attention').multihead_attention(changed,identity,kv,kv,identity,2,kv_heads=1)
        self.close(result[:,0],result2[:,0])

    def test_rope(self):
        module=self.ai('rope');rng=np.random.default_rng(8);x=rng.normal(size=(2,5,6))
        result=module.rope(x);self.close(result[:,0],x[:,0])
        self.close(np.linalg.norm(result,axis=-1),np.linalg.norm(x,axis=-1))
        a,b=rng.normal(size=(1,6)),rng.normal(size=(1,6))
        self.close((module.rope(a,[3])*module.rope(b,[7])).sum(),(module.rope(a,[0])*module.rope(b,[4])).sum())

    def test_lora(self):
        module=self.ai('lora');rng=np.random.default_rng(9)
        x,w,a,b=rng.normal(size=(3,4)),rng.normal(size=(4,5)),rng.normal(size=(4,2)),rng.normal(size=(2,5))
        self.close(module.lora_linear(x,w,a,b,4),x@module.merge(w,a,b,4))

    def test_sampling(self):
        module=self.ai('sampling')
        token,p=module.sample(np.log([.6,.3,.1]),top_p=.7,seed=4)
        self.close(p,[2/3,1/3,0]);self.assertIn(token,[0,1])
        token,p=module.sample([1.,1.,0.],top_k=1,seed=3)
        self.assertEqual(token,0);self.close(p,[1,0,0])
        _,p=module.sample([0.,0.,0.],top_p=1);self.close(p,[1/3]*3)

    def test_beam_search(self):
        def probs(prefix):
            return [math.log(.1),math.log(.6),math.log(.3)] if not prefix else [math.log(.1),math.log(.1),math.log(.8)]
        result=self.ai('beam_search').beam_search(probs,[],2,beam_size=2,max_steps=3)
        self.assertEqual(result[0][0],[1,2]);self.assertAlmostEqual(result[0][1],math.log(.48))
        self.assertEqual(result[1][0],[2])

    def test_kmeans(self):
        x=np.array([[0.,0.],[0.,2.],[10.,10.],[10.,12.]])
        labels,centers=self.ai('kmeans').kmeans(x,2,seed=4)
        self.assertEqual(labels[0],labels[1]);self.assertEqual(labels[2],labels[3]);self.assertNotEqual(labels[0],labels[2])
        self.close(centers[labels[0]],[0,1]);self.close(centers[labels[2]],[10,11])
        labels,centers=self.ai('kmeans').kmeans(np.ones((3,2)),3)
        self.assertTrue(np.isfinite(centers).all())

    def test_knn(self):
        module=self.ai('knn')
        self.close(module.knn([[0],[2],[4]],[1,0,0],[[1]],2),[0])
        self.close(module.knn([[0],[2]],[9,1],[[1]],1),[9])

    def test_linear_regression(self):
        x=np.array([[-2.],[-1.],[0.],[1.],[2.]]);y=2*x[:,0]+3
        w,b,history=self.ai('linear_regression').fit(x,y,learning_rate=.1,steps=300)
        self.close(w,[2],atol=1e-5);self.assertAlmostEqual(b,3,places=5)
        self.assertLess(history[-1],history[0])

    def test_logistic_regression(self):
        x=np.array([[-3.],[-2.],[2.],[3.]]);y=np.array([0,0,1,1])
        w,b=self.ai('logistic_regression').fit(x,y,steps=300)
        self.assertTrue(np.array_equal((x@w+b)>0,y.astype(bool)))

    def test_pca(self):
        x=np.array([[0.,0.],[1.,2.],[2.,4.],[3.,6.]])
        projected,components,mean,variance=self.ai('pca').pca(x,1)
        self.close(projected@components+mean,x)
        self.close(components@components.T,[[1.]])
        self.assertGreater(variance[0],0)

    def test_gaussian_nb(self):
        model=self.ai('gaussian_nb').GaussianNB().fit([[-2],[-1],[3],[4]],[0,0,1,1])
        self.close(model.predict([[-3],[5]]),[0,1])

    def test_auc(self):
        module=self.ai('auc');self.assertAlmostEqual(module.roc_auc([0,0,1,1],[.1,.4,.35,.8]),.75)
        self.assertEqual(module.roc_auc([1,0],[.5,.5]),.5)
        rng=np.random.default_rng(1)
        for _ in range(100):
            y=[0,1]+list(rng.integers(0,2,8));s=list(rng.integers(0,4,10))
            pairs=[(s[i]>s[j])+.5*(s[i]==s[j]) for i in range(10) if y[i] for j in range(10) if not y[j]]
            self.assertAlmostEqual(module.roc_auc(y,s),float(np.mean(pairs)))
        with self.assertRaises(ValueError):module.roc_auc([1,1],[.2,.9])

    def test_average_precision(self):
        module=self.ai('average_precision')
        self.assertAlmostEqual(module.average_precision([1,0,1],[.9,.8,.7]),5/6)
        self.assertAlmostEqual(module.average_precision([1,0,1],[1,1,1]),2/3)
        self.assertEqual(module.average_precision([0,0],[1,0]),0)

    def test_ndcg(self):
        module=self.ai('ndcg');self.assertEqual(module.ndcg([3,2,1],[3,2,1],3),1)
        self.assertLess(module.ndcg([3,2,1],[1,2,3],3),1)
        self.assertEqual(module.ndcg([0,0],[1,2],2),0)

    def test_cosine_topk(self):
        order,scores=self.ai('cosine_topk').cosine_topk([1,0],[[1,0],[0,0],[2,0],[-1,0]],3)
        self.close(order,[0,2,1]);self.close(scores,[1,1,0])

    def test_iou_nms(self):
        module=self.ai('iou_nms');boxes=np.array([[0,0,2,2],[0,0,2,2],[3,3,4,4]])
        self.close(module.iou(boxes[0],boxes),[1,1,0])
        self.assertEqual(module.nms(boxes,[.9,.9,.8]),[0,2])
        self.close(module.iou([0,0,0,0],[[0,0,0,0]]),[0])

    def test_conv2d(self):
        module=self.ai('conv2d');x=np.arange(1.,10.).reshape(1,1,3,3)
        self.close(module.conv2d(x,np.ones((1,1,2,2))),[[[[12,16],[24,28]]]])
        # 非对称核检查互相关与翻转卷积的区别。
        self.close(module.conv2d(x,np.array([[[[1,0],[0,-1]]]])),[[[[-4,-4],[-4,-4]]]])
        self.close(module.conv2d(x,np.ones((1,1,1,1)),bias=[1],stride=2),[[[[2,4],[8,10]]]])

    def test_max_pool2d(self):
        module=self.ai('max_pool2d');x=np.zeros((1,1,3,3));x[0,0,1,1]=9
        y,cache=module.max_pool2d(x,size=2,stride=1);self.close(y,np.full((1,1,2,2),9))
        gradient=module.backward(np.ones_like(y),cache)
        expected=np.zeros_like(x);expected[0,0,1,1]=4;self.close(gradient,expected)

    def test_mlp_backprop(self):
        module=self.ai('mlp_backprop');rng=np.random.default_rng(5)
        x=rng.normal(size=(3,2));y=np.array([0,1,0])
        params=[rng.normal(size=(2,3)),rng.normal(size=3),rng.normal(size=(3,2)),rng.normal(size=2)]
        loss,gradients=module.loss_and_gradients(x,y,*params)
        for index,gradient in enumerate(gradients):
            def objective(z):
                current=params[:];current[index]=z
                return module.loss_and_gradients(x,y,*current)[0]
            self.close(gradient,numeric_gradient(objective,params[index]))

    def test_adam(self):
        optimizer=self.ai('adam').Adam((2,),learning_rate=.1)
        self.close(optimizer.step(np.array([1.,2.]),np.array([2.,-3.])),[.9,2.1])
        self.close(optimizer.step(np.array([1.,2.]),np.array([2.,-3.])),[.9,2.1])

    def test_dropout(self):
        module=self.ai('dropout');x=np.ones((100,))
        y,mask=module.dropout(x,p=.5,seed=2)
        self.assertEqual(set(y),{0.,2.});self.close(module.backward(x,mask),mask)
        self.close(module.dropout(x,p=.5,training=False)[0],x)

    def test_kl_js(self):
        module=self.ai('kl_js');self.assertEqual(module.kl([.2,.8],[.2,.8]),0)
        self.assertEqual(module.kl([1,0],[0,1]),float('inf'))
        self.assertAlmostEqual(module.js([1,0],[0,1]),math.log(2))

    def test_infonce(self):
        loss=self.ai('infonce').infonce(np.eye(2),np.eye(2),temperature=1)
        self.assertAlmostEqual(loss,math.log1p(math.exp(-1)))

    def test_rl_losses(self):
        module=self.ai('rl_losses')
        self.assertAlmostEqual(module.ppo_loss(np.log([1.5,.5]),[0,0],[1,-1]),-.2)
        self.assertAlmostEqual(module.dpo_loss([0],[0],[0],[0]),math.log(2))
        self.close(module.group_advantage([[1,2,3],[2,2,2]]).mean(axis=-1),[0,0])
        self.close(module.group_advantage([[2,2,2]]),[[0,0,0]])

    def test_bpe(self):
        module=self.ai('bpe');rules=module.train({'abab':3},2)
        self.assertEqual(rules,[('a','b'),('ab','ab')])
        self.assertEqual(module.encode('abab',rules),['abab'])
        self.assertEqual(module.encode('abc',rules),['ab','c'])

    def test_reservoir_sampling(self):
        module=self.ai('reservoir_sampling')
        self.assertEqual(module.reservoir_sample(iter([1,2]),4,seed=1),[1,2])
        self.assertEqual(module.reservoir_sample(iter(range(100)),0),[])
        sample=module.reservoir_sample(iter(range(100)),5,seed=1)
        self.assertEqual(len(set(sample)),5);self.assertTrue(all(0<=x<100 for x in sample))
        self.assertEqual(sample,module.reservoir_sample(iter(range(100)),5,seed=1))

    def test_fisher_yates(self):
        values=list(range(20));out=self.ai('fisher_yates').shuffle(values,seed=3)
        self.assertEqual(sorted(out),list(range(20)));self.assertIs(out,values)
        self.assertEqual(out,self.ai('fisher_yates').shuffle(list(range(20)),seed=3))

    def test_focal_loss(self):
        module=self.ai('focal_loss')
        self.assertAlmostEqual(module.focal_loss([0.,0.],[0,1]),.5*.25*math.log(2))
        self.assertTrue(math.isfinite(module.focal_loss([-1000.,1000.],[1,0])))

    def test_soft_nms(self):
        result=self.ai('soft_nms').soft_nms([[0,0,1,1],[0,0,1,1]],[1.,.8],minimum=0)
        self.assertEqual(result[0],(0,1.));self.assertEqual(result[1][0],1)
        self.assertAlmostEqual(result[1][1],.8*math.exp(-2))
