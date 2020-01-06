# https://leetcode-cn.com/problems/subdomain-visit-count/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dct = {}

        def address_decomp(addr):
            subdomain_list = addr.split('.')
            level_num = len(subdomain_list)
            return ['.'.join(subdomain_list[-1 - i:]) for i in range(level_num)]

        for cpdomain in cpdomains:
            times, address = cpdomain.split(' ')
            for subdomain in address_decomp(address):
                if subdomain not in dct:
                    dct[subdomain] = int(times)
                else:
                    dct[subdomain] += int(times)

        return [str(dct[subdomain]) + ' ' + subdomain for subdomain in dct]

