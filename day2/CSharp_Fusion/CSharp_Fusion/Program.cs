using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace CSharp_Fusion
{
    /// <summary>
    /// Classe per il giorno 2 dell'AdventOfCode2021.
    /// Author: Fusion (@manuelandreatta)
    /// </summary>
    class Program
    {
        public static void Main(string[] args)
        {
            Restart:
            Console.WriteLine("Quale esercizio vuoi vedere? (1-2)");
            string input = Console.ReadLine().Trim().ToLower();

            switch (input)
            {
                case "1":
                    Console.Clear();
                    Console.WriteLine("[Esercizio]\nCalcola il numero totale di sequenze incrementali in un array numerico.\n");
                    Exercise1();
                    break;
                case "2":
                    Console.Clear();
                    Console.WriteLine("[Esercizio]\nCalcola il numero totale di sequenze incrementali in una finestra di 3 valori.\n");
                    Exercise2();
                    break;
                default:
                    Console.Clear();
                    Console.WriteLine("[!] Puoi scegliere solo tra 1 e 2.");
                    goto Restart;
            }
        }

        /// <summary>
        /// Sposta il sottomarino seguendo i comandi dell'input e aggiungendo l'aim
        /// </summary>
        private static void Exercise2()
        {
            int depth = 0;
            int horizontalPosition = 0;
            int aim = 0;

            List<string> inputs = File.ReadAllLines("input.txt").ToList();

            foreach (string input in inputs)
            {
                if (input.Contains(" "))
                {
                    string direction = input.Split(' ')[0];
                    int amount = int.Parse(input.Split(' ')[1]);

                    switch (direction)
                    {
                        case "forward":
                            horizontalPosition += amount;
                            depth += aim * amount;
                            break;
                        case "down":
                            aim += amount;
                            break;
                        case "up":
                            aim -= amount;
                            break;
                    }
                }
            }

            Console.WriteLine($"Il sottomarino alla fine del percorso ha una profondità {depth}, una posizione orizzontale {horizontalPosition} e un aim di {aim}.\n\nIl risultato è {horizontalPosition * depth}");
        }

        /// <summary>
        /// Sposta il sottomarino seguendo i comandi dell'input .txt
        /// </summary>
        /// <param name="args"></param>
        private static void Exercise1()
        {
            int depth = 0;
            int horizontalPosition = 0;

            List<string> inputs = File.ReadAllLines("input.txt").ToList();

            foreach (string input in inputs)
            {
                if (input.Contains(" "))
                {
                    string direction = input.Split(' ')[0];
                    int amount = int.Parse(input.Split(' ')[1]);

                    switch (direction)
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
