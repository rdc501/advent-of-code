using System.Runtime.InteropServices.JavaScript;
using System.Text;
using System.Text.RegularExpressions;

namespace _2024;

public class Day4Puzzle1
{
    public static string Execute()
    {
        var lines = File.ReadAllLines("inputs/day4.txt");
        
        var forwardsLines = new List<string>(lines);
        var verticalLines = FlipStrings(forwardsLines);
        var diagonalLines = GetForwardDiagonalStrings(forwardsLines);
        var backwardsDiagonalLines = GetBackwardDiagonalStrings(forwardsLines);

        var allLines = forwardsLines.Concat(verticalLines)
            .Concat(diagonalLines)
            .Concat(backwardsDiagonalLines)
            .ToList();
        
        return allLines.Select(x =>
        {
            var xmasCount = Regex.Matches(x, "XMAS").Count;
            var samxCount = Regex.Matches(x, "SAMX").Count;
            
            return  xmasCount + samxCount;
        }).Sum()
        .ToString();
    }
    
    private static string ReverseString(string input)
    {
        return new string(input.Reverse().ToArray());
    }

    private static List<string> FlipStrings(List<string> input)
    {
        var columns = new List<StringBuilder>();

        foreach (var column in input[0])
        {
            columns.Add(new StringBuilder());
        }

        foreach (var row in input)
        {
            for (var columnIndex = 0; columnIndex < row.Length; columnIndex++)
            {
                columns[columnIndex].Append(row[columnIndex]);
            }
        }

        return columns.Select(x => x.ToString()).ToList();
    }

    private static List<string> GetForwardDiagonalStrings(List<string> input)
    {
        var diagonals = new List<StringBuilder>();
        var diagonalIndexes = new List<List<int>>();

        for (var rowIndex = 0; rowIndex < input.Count; rowIndex++)
        {
            var rowDiagonalIndexes = new List<int>();
            
            for (var columnIndex = 0; columnIndex < input[0].Length; columnIndex++)
            {
                rowDiagonalIndexes.Add(columnIndex - rowIndex);
            }
            
            var index = input[0].Length - 1 + rowIndex;
            var diagonalIndex = 0;

            while (
                diagonalIndex < rowDiagonalIndexes.Count && 
                rowDiagonalIndexes[diagonalIndex] < 0
            )
            {
                rowDiagonalIndexes[diagonalIndex] = index;
                diagonalIndex++;
                index--;
            }

            diagonalIndexes.Add(rowDiagonalIndexes);
        }

        for (var rowIndex = 0; rowIndex < input.Count; rowIndex++)
        {
            for (var columnIndex = 0; columnIndex < input[0].Length; columnIndex++)
            {
                var diagonalIndex = diagonalIndexes[rowIndex][columnIndex];
                
                if (diagonals.Count() - 1< diagonalIndex)
                    diagonals.Add(new StringBuilder());
                
                diagonals[diagonalIndex].Append(input[rowIndex][columnIndex]);
            }
        }
        
        return diagonals.Select(x => x.ToString()).ToList();
    }
    

    private static List<string> GetBackwardDiagonalStrings(List<string> input)
    {
        var diagonals = new List<StringBuilder>();
        var diagonalIndexes = new List<List<int>>();

        for (var rowIndex = 0; rowIndex < input.Count; rowIndex++)
        {
            var rowDiagonalIndexes = new List<int>();
            
            for (var columnIndex = 0; columnIndex < input[0].Length; columnIndex++)
            {
                rowDiagonalIndexes.Add(rowIndex + columnIndex);
            }

            diagonalIndexes.Add(rowDiagonalIndexes);
        }

        for (var rowIndex = 0; rowIndex < input.Count; rowIndex++)
        {
            for (var columnIndex = 0; columnIndex < input[0].Length; columnIndex++)
            {
                var diagonalIndex = diagonalIndexes[rowIndex][columnIndex];
                
                if (diagonals.Count() - 1< diagonalIndex)
                    diagonals.Add(new StringBuilder());
                
                diagonals[diagonalIndex].Append(input[rowIndex][columnIndex]);
            }
        }
        
        return diagonals.Select(x => x.ToString()).ToList();
    }
}