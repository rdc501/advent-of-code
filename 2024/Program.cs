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
                        "day two puzzle two"
                    }));
            
            AnsiConsole.MarkupLine($"[green]Selected:[/] {selectedTask}");
            
             var result = selectedTask switch
            {
                "day one puzzle one" => DayOnePuzzleOne.Execute(),
                "day one puzzle two" => DayOnePuzzleTwo.Execute(),
                "day two puzzle one" => DayTwoPuzzleOne.Execute(),
                "day two puzzle two" => DayTwoPuzzleTwo.Execute(),
                _ => throw new NotImplementedException()
            };
            
            AnsiConsole.MarkupLine($"[green]Result:[/] {result}");
            Console.ReadLine();
        }
    }
}