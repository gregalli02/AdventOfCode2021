using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace CSharp_Fusion
{
    class Program
    {
        /// <summary>
        /// Sposta il sottomarino seguendo i comandi dell'input .txt
        /// </summary>
        /// <param name="args"></param>
        static void Main(string[] args)
        {
            int depth = 0;
            int horizontalPosition = 0;

            List<string> inputs = File.ReadAllLines("input.txt").ToList();

            foreach(string input in inputs)
            {
                if(input.Contains(" "))
                {
                    string direction = input.Split(' ')[0];
                    int amount = int.Parse(input.Split(' ')[1]);

                    switch(direction)
                    {
                        case "forward":
                            horizontalPosition += amount;
                            break;
                        case "down":
                            depth += amount;
                            break;
                        case "up":
                            depth -= amount;
                            break;
                    }
                }
            }

            Console.WriteLine($"Il sottomarino è partito da una posizione orizzontale 0 e da una profondità 0, è arrivato ad una posizione orizzontale {horizontalPosition} e una profondità {depth}.\n\nIl risultato moltiplicato è {horizontalPosition * depth}");
        }
    }
}
