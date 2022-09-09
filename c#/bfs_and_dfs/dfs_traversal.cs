﻿using System;
using System.Collections.Generic;
using System.Text;

namespace bfs_and_dfs
{
    partial class Program
    {
        static void dfs_traversal(Node node)
        {
            // recursive walk on a branch in deep
            if(node == null)
            {
                return;
            }
            Console.Write(node.data + " ");
            dfs_traversal(node.left);
            dfs_traversal(node.right);
        }
    }
}
