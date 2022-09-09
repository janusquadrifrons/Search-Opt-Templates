using System;
using System.Collections.Generic;
using System.Text;

namespace bfs_and_dfs
{
    partial class Program
    {
        static void bfs_traversal(Node node)
        {
            // initialize new instance of empty Queue<T>
            Queue<Node> q = new Queue<Node>(); 

            // add object to the end of Queue<T>
            q.Enqueue(node);

            // do as long as Queue<T> has something in it
            while( q.Count > 0)
            {
                node = q.Dequeue();
                Console.WriteLine(node.data + " ");

                if(node.left != null)
                {
                    q.Enqueue(node.left);
                }

                if(node.right != null)
                {
                    q.Enqueue(node.right);
                }
            }


        }
    }
}
