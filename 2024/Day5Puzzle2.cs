namespace _2024;

public class Day5Puzzle2
{
    public static string Execute()
    {
        var lines = File.ReadAllLines("inputs/day5.txt");
        var rules = new List<(int before, int after)>();
        var updates = new List<List<int>>();
        var correctedUpdates = new List<List<int>>();

        foreach (var line in lines)
        {
            if (line.Contains("|"))
            {
                var parts = line.Split("|");
                rules.Add((int.Parse(parts[0]), int.Parse(parts[1])));
            }

            if (line.Contains(","))
            {
                var parts = line.Split(",");
                updates.Add(parts.Select(int.Parse).ToList());
            }
        }

        foreach (var update in updates)
        {
            var relevantRules = GetRelevantRules(rules, update);

            if (!IsUpdateCorrect(relevantRules, update))
                correctedUpdates.Add(CorrectUpdate(relevantRules,update));
        }
        
        return correctedUpdates.Select(x => x[x.Count/2])
            .Sum()
            .ToString();
    }

    private static List<(int before, int after)> GetRelevantRules
    (
        List<(int before, int after)> rules,
        List<int> update
    )
    {
        return rules.Where(x => update.Contains(x.before) &&
                                update.Contains(x.after)
        ).ToList();
    }
    
    private static bool IsUpdateCorrect
    (
        List<(int before, int after)> rules,
        List<int> update
    )
    {
        return rules.All(rule => update.IndexOf(rule.before) <= update.IndexOf(rule.after));
    }

    private static List<int> CorrectUpdate(
        List<(int before, int after)> rules,
        List<int> update
    )
    {
        var newUpdate = new List<int>(update);
        
        while (!IsUpdateCorrect(rules, newUpdate))
        {
            foreach (var rule in rules)
            {
                if (newUpdate.IndexOf(rule.before) > newUpdate.IndexOf(rule.after))
                {
                    newUpdate.RemoveAt(newUpdate.IndexOf(rule.before));
                    newUpdate.Insert(newUpdate.IndexOf(rule.after), rule.before);
                }
            }
        }  
        
        return newUpdate;
    }
}