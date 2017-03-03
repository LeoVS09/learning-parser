
class Builder:
    @classmethod
    def tree(self, data):
        return self.clear_tree(self.build_branch(data))

    @classmethod
    def build_tree(self, tree):
        tree["begin"] = self.build_branch(tree["begin"])
        tree["end"] = self.build_branch(tree["end"])
        return tree

    @classmethod
    def build_branch(self, variants):
        overall = self.search_overall_in_array(variants)
        branches = []
        if overall != -1:
            branch = {
                'begin': [],
                'overall': overall,
                'end': []
            }
            for word in variants:
                start = word.find(overall)
                if start != -1:
                    if start == 0:
                        branch['begin'].append(-1)
                    else:
                        branch['begin'].append(word[:start])
                    end = start + len(overall)
                    if end < len(word):
                        branch['end'].append(word[end:])
                    else:
                        branch['end'].append(-1)
                else:
                    branches.append(word)
            branches.append(self.build_tree(branch))
            return branches
        else:
            return variants

    @classmethod
    def search_overall_in_array(self, array):
        max = ""
        for i in range(len(array)):
            for k in range(i + 1, len(array)):
                overall = self.search_overall_in_words(array[i], array[k])
                if overall != -1 and len(overall) > len(max):
                    max = overall
        if max != "":
            return max
        else:
            return -1

    @classmethod
    def search_overall_in_words(self, first, second):
        if first == -1 or second == -1: return -1
        for k in range(len(first)):
            start = 0
            end = len(first) - k
            overall = first[start:end]
            if second.find(overall) != -1: return overall
            for offset in range(1, k):
                start += offset
                end += offset
                overall = first[start:end]
                if second.find(overall) != -1: return overall
        return -1

    @classmethod
    def clear_tree(self, tree):
        if type(tree) == type(list()):
            while tree.count(-1) > 1:
                tree.remove(-1)
            if len(tree) == 1:
                return tree[0]
            else:
                for leaf in tree:
                    if type(leaf) == type(dict()):
                        for key, el in leaf.items():
                            leaf[key] = self.clear_tree(el)
        return tree