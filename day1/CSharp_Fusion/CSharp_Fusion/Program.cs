using System;
using System.IO;

namespace CSharp_Fusion
{
    /// <summary>
    /// Classe per il giorno 1 dell'AdventOfCode2021.
    /// Author: Fusion (@manuelandreatta)
    /// </summary>
    public class Program
    {
        public static void Main(string[] args)
        {
            Restart:
            Console.WriteLine("Quale esercizio vuoi vedere? (1-2)");
            string input = Console.ReadLine().Trim().ToLower();

            switch(input)
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
        /// Calcola il numero totale di sequenze incrementali in una finestra di 3 valori.
        /// </summary>
        private static void Exercise2()
        {
            int count = 0;

            int[] depths = Array.ConvertAll(File.ReadAllLines("input_1.txt"), obj => int.Parse(obj));

            for (int index = 0; index < depths.Length - 3; index++)
            {
                int firstSum = depths[index] + depths[index + 1] + depths[index + 2];
                int secondSum = depths[index + 3] + depths[index + 1] + depths[index + 2];

                if (secondSum > firstSum)
                    count++;
            }

            Console.WriteLine($"Risultato: {count}");
        }

        /// <summary>
        /// Calcola il numero totale di sequenze incrementali in un array numerico
        /// </summary>
        private static void Exercise1()
        {
            int count = 0;

            int[] depths = Array.ConvertAll(File.ReadAllLines("input_1.txt"), obj => int.Parse(obj));

            for (int index = 0; index < depths.Length - 1; index++)
            {
                int depth = depths[index];
                int nextDepth = depths[index + 1];

                if (nextDepth > depth)
                    count++;
            }

            Console.WriteLine($"Risultato: {count}");
        }
    }
}
