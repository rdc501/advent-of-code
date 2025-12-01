namespace _2024;

public class Day1Puzzle2
{
    public static string Execute()
    {
        var (firstList, secondList) = Day1Puzzle1.GetSortedLists();

        var result = 0;
        
        var cache = new Dictionary<int, int>();
        
        foreach (var item in firstList)
        {
            if (cache.TryGetValue(item, out var value))
                result += item * value;
            
            var firstInstanceIndex = GetFirstInstanceIndex(item, secondList);

            if (firstInstanceIndex is not null)
            {
                secondList = secondList[(int)firstInstanceIndex..];
                
                var numberOfMatches = NumberOfMatches(item, secondList);
                
                cache[item] = numberOfMatches;
                result += item * numberOfMatches;
                secondList = secondList[numberOfMatches..];
            }
        }
        
        return result.ToString();
    }

    private static int? GetFirstInstanceIndex(int value, List<int> list)
    {
        var result = (int?)null;

        for (var i = 0; i < list.Count; i++)
        {
            if (list[i] == value)
            {
                result = i;
                break;
            }

            if (list[i] > value)
            {
                break;
            }
        }
        
        return result;
    }

    private static int NumberOfMatches(int value, List<int> list)
    {
        var result = 0;

        foreach (var t in list)
        {
            if (t != value)
                break;

            result++;
        }
        
        return result;
    }
}