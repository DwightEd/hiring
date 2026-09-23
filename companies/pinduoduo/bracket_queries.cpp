// 括号串翻转与合法查询；完整题面见 04_bracket_queries.md。
// 与 Python 相同的 sum/minPrefix/maxPrefix + lazy flip，供严格时限使用。
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Summary {
    int sum = 0, low = 0, high = 0;
};

Summary merge_summary(const Summary& a, const Summary& b) {
    return {a.sum + b.sum,
            min(a.low, a.sum + b.low),
            max(a.high, a.sum + b.high)};
}

class BracketTree {
    int n;
    vector<Summary> tree;
    vector<unsigned char> lazy;

    void apply(int p) {
        auto& item = tree[p];
        item.sum = -item.sum;
        int old_low = item.low;
        item.low = -item.high;
        item.high = -old_low;
        lazy[p] ^= 1;
    }

    void push(int p) {
        if (lazy[p]) {
            apply(p * 2);
            apply(p * 2 + 1);
            lazy[p] = 0;
        }
    }

    void build(int p, int l, int r, const string& s) {
        if (l == r) {
            int value = s[l] == '(' ? 1 : -1;
            tree[p] = {value, min(0, value), max(0, value)};
            return;
        }
        int mid = (l + r) / 2;
        build(p * 2, l, mid, s);
        build(p * 2 + 1, mid + 1, r, s);
        tree[p] = merge_summary(tree[p * 2], tree[p * 2 + 1]);
    }

    void flip(int p, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) {
            apply(p);
            return;
        }
        push(p);
        int mid = (l + r) / 2;
        if (ql <= mid) flip(p * 2, l, mid, ql, qr);
        if (qr > mid) flip(p * 2 + 1, mid + 1, r, ql, qr);
        tree[p] = merge_summary(tree[p * 2], tree[p * 2 + 1]);
    }

    Summary query(int p, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return tree[p];
        push(p);
        int mid = (l + r) / 2;
        if (qr <= mid) return query(p * 2, l, mid, ql, qr);
        if (ql > mid) return query(p * 2 + 1, mid + 1, r, ql, qr);
        // 合并顺序必须是左片段在前、右片段在后。
        return merge_summary(query(p * 2, l, mid, ql, qr),
                             query(p * 2 + 1, mid + 1, r, ql, qr));
    }

public:
    explicit BracketTree(const string& s)
        : n(static_cast<int>(s.size())), tree(4 * n), lazy(4 * n, 0) {
        build(1, 0, n - 1, s);
    }

    // 对外使用 0-based 半开区间 [left, right)。
    void flip(int left, int right) { flip(1, 0, n - 1, left, right - 1); }

    bool valid(int left, int right) {
        if ((right - left) & 1) return false;
        Summary result = query(1, 0, n - 1, left, right - 1);
        return result.sum == 0 && result.low >= 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    string s;
    cin >> n >> q >> s;
    BracketTree tree(s);
    while (q--) {
        char operation;
        int left, right;
        cin >> operation >> left >> right;
        --left;
        if (operation == 'F') tree.flip(left, right);
        else cout << (tree.valid(left, right) ? "YES\n" : "NO\n");
    }
}
