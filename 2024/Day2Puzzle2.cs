namespace _2024;

public static class Day2Puzzle2
{
    public static string Execute()
    {
        var lines = File.ReadAllLines("inputs/day_two.txt");

        var count = lines.Select(line => line.Split(" ")
                .Where(x => !string.IsNullOrWhiteSpace(x))
                .Select(int.Parse)
                .ToList())
            .Count(IsReportSafe);

        return count.ToString();
    }

    private static bool IsReportSafe(List<int> report)
    {
        var x = new List<int>();

        for (var i = 0; i < report.Count; i++)
        {
            var newReport = new List<int>(report);
            newReport.RemoveAt(i);

            x.Add(GetFailedLevels(newReport).Count);
        }

        return x.Contains(0);
    }

    private static List<int> GetFailedLevels(List<int> report)
    {
        const int minSafeDiff = 1;
        const int maxSafeDiff = 3;
        
        var increasing = report[0] < report[1];
    
        var result = new List<int>();
    
        for (var i = 1; i < report.Count; i++)
        {
            if (increasing != report[i - 1] < report[i])
            {
                result.Add(i);
                continue;
            }
            
            var diff = Math.Abs(report[i] - report[i - 1]);
    
            if (diff < minSafeDiff || diff > maxSafeDiff)
            {
                result.Add(i);
            }
        }
        
        return result;
    }
}