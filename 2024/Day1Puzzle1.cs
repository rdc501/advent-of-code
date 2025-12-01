namespace _2024;

public static class Day1Puzzle1
{
    public static string Execute()
    {
        var (firstList, secondList) = GetSortedLists();
        
        var result = firstList.Select((t, i) => Math.Abs(t - secondList[i])).Sum();

        return result.ToString();
    }
    
    public static (List<int>, List<int>) GetSortedLists()
    {
        var lines = File.ReadAllLines("inputs/day_one.txt");

        var firstList = new List<int>();
        var secondList = new List<int>();

        foreach (var line in lines)
        {
            var items = line.Split(" ")
                .Where(x => !string.IsNullOrWhiteSpace(x))
                .Select(int.Parse)
                .ToList();
            
            firstList.Add(items[0]);
            secondList.Add(items[1]);
        }
        
        firstList.Sort();
        secondList.Sort();

        return (firstList, secondList);
    }
}