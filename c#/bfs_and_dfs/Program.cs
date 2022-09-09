using bfs_and_dfs;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bfs_and_dfs
{
    partial class Program
    {
        /*
         *                       A
         *                     /   \ 
         *                    B     E
         *                   / \   / \
         *                  C   D F   G
         *                             \
         *                              H
         * */


        static Node sample_tree()
        {
            Node root =
                new Node("A",
                new Node("B",
                    new Node("C"), new Node("D")),
                new Node("E",
                    new Node("F"), new Node("G",
                        new Node("H"), null)));
            return root;
        }

        static void Main(string[] args)
        {
            Node tree = sample_tree();

            // Uncomment for BFS ↓
            // Console.WriteLine("BFS →"); bfs_traversal(tree);

            //Uncomment for DFS ↓
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("\r\nDFS →"); dfs_traversal(tree);
        }
    }
}
