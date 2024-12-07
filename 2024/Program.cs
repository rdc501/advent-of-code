using Spectre.Console;

namespace _2024;

public static class Program
{
    public static void Main(string[] args)
    {
        while (true) {
            var selectedTask = AnsiConsole.Prompt(
                new SelectionPrompt<string>()
                    .Title("[green]What puzzle do you want to run?[/]")
                    .PageSize(10)
                    .MoreChoicesText("[grey](Move up and down to reveal more)[/]")
                    .AddChoices(new[] {
                        "day one puzzle one",
                        "day one puzzle two",
                        "day two puzzle one",
                        "day two puzzle two",
                        "day three puzzle one",
                        "day three puzzle two",
                        "day four puzzle one",
                        "day four puzzle two"
                    }));
            
            AnsiConsole.MarkupLine($"[green]Selected:[/] {selectedTask}");
            
             var result = selectedTask switch
            {
                "day one puzzle one" => Day1Puzzle1.Execute(),
                "day one puzzle two" => Day1Puzzle2.Execute(),
                "day two puzzle one" => Day2Puzzle1.Execute(),
                "day two puzzle two" => Day2Puzzle2.Execute(),
                "day three puzzle one" => Day3Puzzle1.Execute(),
                "day three puzzle two" => Day3Puzzle2.Execute(),
                "day four puzzle one" => Day4Puzzle1.Execute(),
                "day four puzzle two" => Day4Puzzle2.Execute(),
                _ => throw new NotImplementedException()
            };
            
            AnsiConsole.MarkupLine($"[green]Result:[/] {result}");
            Console.ReadLine();
        }
    }
}