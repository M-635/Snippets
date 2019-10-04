static public string FormatRut(string myString)
        {
            string Rut = new String(myString.Where(Char.IsDigit).ToArray());
            if (Rut.Length == 7)
            {
                if (myString.Contains("k"))
                {
                    Rut = Rut.Substring(0, 7) + "k";
                    return myString.Substring(0, 1)
                    + "."
                    + Rut.Substring(1, 3)
                    + "."
                    + Rut.Substring(4, 3)
                    + "-"
                    + Rut.Substring(7, 1);
                }
                else
                    return null;
                }
            }
            if (Rut.Length == 8)
            {
                if (myString.Contains("k"))
                {
                    Rut = Rut.Substring(0, 8) + "k";
                    return myString.Substring(0, 2)
                    + "."
                    + Rut.Substring(2, 3)
                    + "."
                    + Rut.Substring(5, 3)
                    + "-"
                    + Rut.Substring(8, 1);
                }
                else
                {
                    return myString.Substring(0, 1)
                    + "."
                    + Rut.Substring(1, 3)
                    + "."
                    + Rut.Substring(4, 3)
                    + "-"
                    + Rut.Substring(7, 1);
                }
            }
            if (Rut.Length == 9)
            {
                return Rut.Substring(0, 2)
                + "."
                + Rut.Substring(2, 3)
                + "."
                + Rut.Substring(5, 3)
                + "-"
                + Rut.Substring(8, 1);
            }
            else
            {
                return null;
            }
        }