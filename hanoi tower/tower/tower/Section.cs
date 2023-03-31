namespace Hanoi
{
    public class Section
    {
        public int Weight { get; set; }
        public int Tower { get; set; }
        public int Number { get; set; }
        public int NumberInTower { get; set; }
        public Section(int weight, int tower, int number)
        {
            Weight = weight;
            NumberInTower = number;
            Tower = tower;
            Number = number;
        }
        public void Rearrange(int tower, List<Section> sections)
        {
            if (tower <= 0 || tower >3) throw new Exception(Consts.UncorrectableTower);
            if (Tower == tower) throw new Exception(Consts.EqualTower);
            List<Section> OutTowerSections = sections.FindAll(x => x.Tower == Tower);
            if (OutTowerSections.Count == 0)
            {
                throw new Exception(Consts.ExceptionNotFound);
            }
            if (OutTowerSections.Any(x=> x.Weight < Weight)) throw new Exception(Consts.ExceptionLowwerWeightFoundinOutTower);
            List<Section> OnTowerSections = sections.FindAll(x=>x.Tower == tower);
            if (OnTowerSections.Count == 0)
            {
                Tower = tower;
                NumberInTower = 1;
                Program.Draw();
                return;
            }
            if (OnTowerSections.SingleOrDefault(x=>x.Weight <= Weight) is null)
            {
                Tower = tower;
                NumberInTower = OnTowerSections.Select(x=> x.NumberInTower).Max()+1;
                Program.Draw();
                return;
            }
            throw new Exception(Consts.ExceptionLowwerWeightFoundInOnTower);
        }
    }
}
