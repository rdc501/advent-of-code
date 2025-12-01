namespace _2024;

public static class DayTwoPuzzleOne
{
    public static string Execute()
    {
        var lines = File.ReadAllLines("inputs/day_two_puzzle_one.txt");

        var count = lines.Select(line => line.Split(" ")
                .Where(x => !string.IsNullOrWhiteSpace(x))
                .Select(int.Parse)
                .ToList())
            .Count(IsReportSafe);

        return count.ToString();
    }

    public static bool IsReportSafe(List<int> report)
    {
        const int minSafeDiff = 1;
        const int maxSafeDiff = 3;
        var increasing = report[0] < report[1];

        var result = true;

        for (var i = 1; i < report.Count; i++)
        {
            if (increasing != report[i - 1] < report[i])
            {
                result = false;
                break;
            }
            
            var diff = Math.Abs(report[i] - report[i - 1]);

            if (diff < minSafeDiff || diff > maxSafeDiff)
            {
                result = false;
                break;
            }
        }
        
        return result;
    }
}