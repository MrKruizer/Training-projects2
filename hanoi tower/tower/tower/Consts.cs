namespace Hanoi
{
    public static class Consts
    {
        // Exceptions
        public static string ExceptionNotFound = "Ошибка, не удалось найти искомую секцию башни.";
        public static string ExceptionLowwerWeightFoundInOnTower = "В этой башне находятся меньшие секции.";
        public static string ExceptionLowwerWeightFoundinOutTower = "Вы не можете переносить секцию, на которой расположены меньшие секции.";
        public static string EqualTower = "Номер башни, на которую переносится секция, совпадает с исходным.";
        public static string UncorrectableTower = "Некорректное значение номера башни.";
        // Text
        public static string StartText = "Чтобы начать игру введите какую секцию выхотите перенести и на какую башню. Пример: 5 to 3. Clear для восстановления башни. Auto для проигрывания примера.";
        public static string Columns = "Секции в башнее отображаются в виде Номер секции/Вес секции";
        public static string End = "Спасибо за игру.";
        //Re
        public static string Layer = " {t1}   {t2}   {t3} ";
        //Commands
        public static string Quit = "Quit";
        public static string Auto = "Auto";
        public static string Clear = "Clear";

        // Int
        public static int CommonCountSections = 5;
    }
}
