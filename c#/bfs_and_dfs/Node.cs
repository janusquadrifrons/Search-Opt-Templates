using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bfs_and_dfs
{
    public class Node
    {
        public Node left;
        public Node right;
        public String data;

        // class constructors
        public Node(String data, Node left, Node right)
        {
            this.data = data;
            this.left = left;
            this.right = right;
        }

        public Node(String data)
        {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }
}