


using System.Text.RegularExpressions;

namespace Hanoi
{
    internal class Program
    {
        internal static List<Section> Sections;
        internal static Regex StepMatch = new Regex($@"\d to \d");
        static void Main(string[] args)
        {
            Sections = GenerateTower();
            Draw();
            Play();
            Console.WriteLine("")
        }
        public static void Draw()
        {
            Console.WriteLine(Consts.Columns);
            for (int i = 0; i < Consts.CommonCountSections; i++)
            {
                var layer = Sections.Where(x=> x.NumberInTower == Consts.CommonCountSections - i);
                Console.WriteLine(Consts.Layer
                    .Replace("{t1}", layer.Any(x=> x.Tower == 1) ? string.Join('/',layer.Where(x => x.Tower == 1).SelectMany(x=> new List<int>() { x.Number, x.Weight })) : "|")
                    .Replace("{t2}", layer.Any(x => x.Tower == 2) ? string.Join('/', layer.Where(x => x.Tower == 2).SelectMany(x => new List<int>() { x.Number, x.Weight })) : "|")
                    .Replace("{t3}", layer.Any(x => x.Tower == 3) ? string.Join('/', layer.Where(x => x.Tower == 3).SelectMany(x => new List<int>() { x.Number, x.Weight })) : "|"));
            }
        }
        static void Play()
        {
            Console.WriteLine(Consts.StartText);
            do
            {
                string input = Console.ReadLine();
                if (string.IsNullOrEmpty(input?.Trim())) continue;
                input = input.Trim();
                if (input == Consts.Quit) break;
                if (StepMatch.IsMatch(input))
                {
                    var strings = input.Split(" ");
                    if (int.TryParse(strings[0], out int number) && int.TryParse(strings[2], out int tower))
                    {
                        if (number > Sections.Count) Console.WriteLine(Consts.ExceptionNotFound);
                        else if (tower > 3 || tower < 1) Console.WriteLine(Consts.UncorrectableTower);
                        else
                        {
                            try
                            {
                                Sections[number - 1].Rearrange(tower, Sections);
                            }
                            catch (Exception ex)
                            {
                                Console.WriteLine(ex.Message);
                            }
                        }
                    }
                }
                else if (input == Consts.Auto)
                {
                    Sections.Clear();
                    Sections.AddRange(GenerateTower());
                    Draw();
                    Auto(1,3);
                }
            } while (true);
        }
        static void Auto(int number, int tower)
        {
            if (number <= 0 || number > Sections.Count) return;
            if (Sections[number-1].Tower == 1 && tower == 3)
            {
                Auto(number + 1, 2);
                Sections[number - 1].Rearrange(tower, Sections);
                Auto(number + 1, 3);
            }
            else if (Sections[number - 1].Tower == 1 && tower == 2)
            {
                Auto(number + 1, 3);
                Sections[number - 1].Rearrange(tower, Sections);
                Auto(number + 1, 2);
            }
            else if (Sections[number - 1].Tower == 2 && tower == 3)
            {
                Auto(number + 1, 1);
                Sections[number - 1].Rearrange(tower, Sections);
                Auto(number + 1, 3);
            }
            else if (Sections[number - 1].Tower == 2 && tower == 1)
            {
                Auto(number + 1, 3);
                Sections[number - 1].Rearrange(tower, Sections);
                Auto(number + 1, 1);
            }
            else if (Sections[number - 1].Tower == 3 && tower == 1)
            {
                Auto(number + 1, 2);
                Sections[number - 1].Rearrange(tower, Sections);
                Auto(number + 1, 1);
            }
            else if (Sections[number - 1].Tower == 3 && tower == 2)
            {
                Auto(number + 1, 1);
                Sections[number - 1].Rearrange(tower, Sections);
                Auto(number + 1, 2);
            }
        }
        static List<Section> GenerateTower()
        {
            var list = new List<Section>();
            for (int i = 0; i < Consts.CommonCountSections; i++)
            {
                list.Add(new Section(Consts.CommonCountSections - i, 1, i + 1));
            }
            return list;
        }
    }
}
