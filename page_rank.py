import numpy

import pdb

class PageRank():
    def __init__(self, graph, _lambda):
        # pdb.set_trace()
        self.graph = graph
        self.N = self.graph.N
        self._lambda = _lambda

        initial_pr = 10000
        self.current_pr = [initial_pr for i in range(self.N)]
        self.new_pr = [0 for i in range(self.N)]

        self.iterate()

    def iterate(self):
        t1 = (1 - self._lambda) / self.N
        flag_continue_to_update_pr = True

        count = 0
        # while(flag_continue_to_update_pr):
        while (count < 50):
            print "*********** NEW ITERATION %d ***********\n" % count
            for i in range(self.N):
                new_weight = t1

                incoming_nodes = self.graph.incoming_of(i)
                # print incoming_nodes

                sum_pr = 0
                for node in incoming_nodes:
                    # print "\ni = %d \t Node = %d PR = %f" % (i, node, self.get_pr(node))
                    # print "Outgoing %d" % self.graph.count_outgoing_of(node)
                    sum_pr += (self.get_pr(node) / self.graph.count_outgoing_of(node))
                    # print sum_pr

                # print "2nd term: %f" % sum_pr
                new_weight = t1 + self._lambda * sum_pr

                # set new_weight
                self.set_new_pr(i, new_weight)

            # finish iteration, set current_pr to the new_pr
            flag_continue_to_update_pr = self.boolean_continue_updating_pr()
            self.verify_pr()
            self.update_pr()

            count += 1

    def get_pr(self, node_id):
        try:
            return self.current_pr[node_id]
        except KeyError:
            print "ERROR get pagerank"

    def set_new_pr(self, node_id, w):
        self.new_pr[node_id] = w

    def boolean_continue_updating_pr(self):
        sum_difference = sum(numpy.subtract(self.current_pr, self.new_pr))

        if sum < 0.1:
            return False
        else:
            return True

    def verify_pr(self):
        s = numpy.sum(self.new_pr)
        print s
        # if s < 0.9 or s > 1.1:
        #     print "PR Error\n"

    def update_pr(self):
        self.current_pr = self.new_pr
        # print self.current_pr
        self.new_pr = [0 for i in range(self.N)]

