using System.ComponentModel;

namespace _2024;

public class Day6Puzzle1
{
    public static string Execute()
    {
        var lines = File.ReadAllLines("inputs/day6.txt").Select(x => x.ToCharArray()).ToList();

        var currentLocation = FindGuard(lines);
        var guardPresent = true;

        while (guardPresent)
        {
            currentLocation = MoveGuard(lines, currentLocation);
            guardPresent = IsGuardPresent(lines, currentLocation);
        }
        
        return "six";
    }

    private static (int rowIndex, int colIndex) FindGuard(List<char[]> lines)
    {
        
        var result = (rowIndex: 0, colIndex: 0);

        for (var rowIndex = 0; rowIndex < lines.Count; rowIndex++)
        {
            var guardIndex = Array.FindIndex(lines[rowIndex], x => x == '^');

            if (guardIndex > -1)
            {
                result = (rowIndex, guardIndex);
                break;
            }
        }

        return result;
    }

    private static (int rowIndex, int colIndex)  MoveGuard(List<char[]> lines, (int rowIndex, int colIndex) currentLocation)
    {
        var nextLocation = currentLocation;

        if (lines[currentLocation.rowIndex][currentLocation.colIndex] == '^')
        {
            if (lines[currentLocation.rowIndex - 1][currentLocation.colIndex] == '#')
            {
                lines[currentLocation.rowIndex][currentLocation.colIndex] = '>';
            }
            else
            {
                nextLocation.rowIndex--;
            }
        }

        if (lines[currentLocation.rowIndex][currentLocation.colIndex] == '>')
        {
            if (lines[currentLocation.rowIndex][currentLocation.colIndex + 1] == '#')
            {
                lines[currentLocation.rowIndex][currentLocation.colIndex] = 'V';
            }
            else
            {
                nextLocation.colIndex++;
            }
        }

        if (lines[currentLocation.rowIndex][currentLocation.colIndex] == 'V')
        {
            if (lines[currentLocation.rowIndex + 1][currentLocation.colIndex] == '#')
            {
                lines[currentLocation.rowIndex][currentLocation.colIndex] = '<';
            }
            else
            {
                nextLocation.rowIndex++;
            }
        }

        if (lines[currentLocation.rowIndex][currentLocation.colIndex] == '<')
        {
            if (lines[currentLocation.rowIndex][currentLocation.colIndex - 1] == '#')
            {
                lines[currentLocation.rowIndex][currentLocation.colIndex] = '^';
            }
            else
            {
                nextLocation.colIndex--;
            }
        }

        if (nextLocation != currentLocation)
            lines[currentLocation.rowIndex][currentLocation.colIndex] = 'X';

        return nextLocation;
    }

    private static bool IsGuardPresent(List<char[]> lines, (int rowIndex, int colIndex) currentLocation)
    {
        return currentLocation.rowIndex < 0 ||
               currentLocation.rowIndex >= lines.Count ||
               currentLocation.colIndex < 0 ||
               currentLocation.colIndex >= lines[0].Length;
    }
}