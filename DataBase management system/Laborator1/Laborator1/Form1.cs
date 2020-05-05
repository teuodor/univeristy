using Laborator1.Repository;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Laborator1
{
    public partial class Form1 : Form
    {
        private static string conn = "Data Source=DESKTOP-SIFAM82\\MSSQLSERVER01;Initial Catalog=VinylSqlShop1;Integrated Security=True";
        SqlConnection sqlConnection = new SqlConnection(conn);
        SqlDataAdapter sqlAdapterCrate = new SqlDataAdapter();
        SqlDataAdapter sqlAdapterVinyl = new SqlDataAdapter();
        DataSet dataSet1 = new DataSet();
        DataSet dataSet= new DataSet();
        //un data set

        public Form1()
        {
            InitializeComponent();

        }

        private void crateView_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            try
            {
                crateView.CurrentRow.Selected = true;
                int id = Int32.Parse(crateView.Rows[e.RowIndex].Cells["IdCrate"].FormattedValue.ToString());
                sqlConnection.Open();
                sqlAdapterVinyl.SelectCommand = new SqlCommand("SELECT * FROM Vinyl WHERE IdCrate = @IdCrate", sqlConnection);
                sqlAdapterVinyl.SelectCommand.Parameters.Add("@IdCrate", SqlDbType.Int);
                sqlAdapterVinyl.SelectCommand.Parameters["@IdCrate"].Value = id;

                dataSet.Clear();
                sqlAdapterVinyl.Fill(dataSet);
                vinylView.DataSource = dataSet.Tables[0];
                sqlConnection.Close();
            }
            catch(Exception)
            {
                Console.WriteLine("Eroare Crate View");
            }
        }


        private void showCratesButton_Click(object sender, EventArgs e)
        {
            try
            {
                sqlConnection.Open();
                sqlAdapterCrate.SelectCommand = new SqlCommand("SELECT * FROM CRATE", sqlConnection);
                dataSet1.Clear();
                sqlAdapterCrate.Fill(dataSet1);
                crateView.DataSource = dataSet1.Tables[0];
                sqlConnection.Close();
            }
            catch(Exception)
            {
                Console.WriteLine("Eroare Show Crate Button");
            }
        }

        private void addVinylButton_Click(object sender, EventArgs e)
        {
            try
            {
                sqlConnection.Open();
                sqlAdapterVinyl.SelectCommand = new SqlCommand("INSERT INTO Vinyl VALUES ((SELECT MAX(IdVinyl) FROM Vinyl) + 1, @Name, @Genre, @Price, @IdCrate)", sqlConnection);
                string name = nameTextBox.Text;
                string genre = genreTextBox.Text;
                int price = Int32.Parse(priceTextBox.Text);

                if (crateView.SelectedCells.Count > 0 || name.CompareTo("") == 0 || genre.CompareTo("") == 0 || price == 0)
                {
                    int selectedrowindex = crateView.SelectedCells[0].RowIndex;
                    DataGridViewRow selectedRow = crateView.Rows[selectedrowindex];
                    int idCrate = Int32.Parse(Convert.ToString(selectedRow.Cells["IdCrate"].Value));

                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@Name", SqlDbType.VarChar);
                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@Genre", SqlDbType.VarChar);
                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@Price", SqlDbType.Int);
                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@IdCrate", SqlDbType.Int);

                    sqlAdapterVinyl.SelectCommand.Parameters["@Name"].Value = name;
                    sqlAdapterVinyl.SelectCommand.Parameters["@Genre"].Value = genre;
                    sqlAdapterVinyl.SelectCommand.Parameters["@Price"].Value = price;
                    sqlAdapterVinyl.SelectCommand.Parameters["@IdCrate"].Value = idCrate;

                    sqlAdapterVinyl.SelectCommand.ExecuteNonQuery();

                    sqlAdapterVinyl.SelectCommand = new SqlCommand("SELECT * FROM Vinyl WHERE IdCrate = @IdCrate", sqlConnection);
                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@IdCrate", SqlDbType.Int);
                    sqlAdapterVinyl.SelectCommand.Parameters["@IdCrate"].Value = idCrate;

                    dataSet.Clear();
                    sqlAdapterVinyl.Fill(dataSet);
                    vinylView.DataSource = dataSet.Tables[0];

                    sqlConnection.Close();
                }
                else
                {
                    sqlConnection.Close();
                    throw new Exception();
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Eroare Button Vinyl");
            }
        }

        private void delButton_Click(object sender, EventArgs e)
        {
            try
            {
                sqlConnection.Open();
                sqlAdapterVinyl.SelectCommand = new SqlCommand("DELETE FROM Vinyl WHERE IdVinyl = @IdVinyl",sqlConnection);
                if(vinylView.SelectedCells.Count > 0)
                {
                    int selectedRowIndex = vinylView.SelectedCells[0].RowIndex;
                    DataGridViewRow selectedRow = vinylView.Rows[selectedRowIndex];
                    int idVinyl = Int32.Parse(Convert.ToString(selectedRow.Cells["IdVinyl"].Value));

                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@IdVinyl", SqlDbType.Int);
                    sqlAdapterVinyl.SelectCommand.Parameters["@IdVinyl"].Value = idVinyl;

                    sqlAdapterVinyl.SelectCommand.ExecuteNonQuery();

                    int idCrate = Int32.Parse(Convert.ToString(selectedRow.Cells["IdCrate"].Value));
                    sqlAdapterVinyl.SelectCommand = new SqlCommand("SELECT * FROM Vinyl WHERE IdCrate = @IdCrate", sqlConnection);
                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@IdCrate", SqlDbType.Int);
                    sqlAdapterVinyl.SelectCommand.Parameters["@IdCrate"].Value = idCrate;

                    dataSet.Clear();
                    sqlAdapterVinyl.Fill(dataSet);
                    vinylView.DataSource = dataSet.Tables[0];

                    sqlConnection.Close();
                }
                else
                {
                    sqlConnection.Close();
                    throw new Exception();
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Eroare Button delete");
            }
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            try
            {
                sqlConnection.Open();
                sqlAdapterVinyl.SelectCommand = new SqlCommand("UPDATE Vinyl SET NameOf = @Name, Genre = @Genre, Price = @Price WHERE IdVinyl = @IdVinyl", sqlConnection);
                if (vinylView.SelectedCells.Count > 0)
                {
                    int selectedRowIndex = vinylView.SelectedCells[0].RowIndex;
                    DataGridViewRow selectedRow = vinylView.Rows[selectedRowIndex];
                    int idVinyl = Int32.Parse(Convert.ToString(selectedRow.Cells["IdVinyl"].Value));

                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@Name", SqlDbType.VarChar);
                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@Genre", SqlDbType.VarChar);
                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@Price", SqlDbType.Int);
                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@IdVinyl", SqlDbType.Int);

                    string name = nameTextBox.Text;
                    string genre = genreTextBox.Text;
                    int price = Int32.Parse(priceTextBox.Text);

                    sqlAdapterVinyl.SelectCommand.Parameters["@Name"].Value = name;
                    sqlAdapterVinyl.SelectCommand.Parameters["@Genre"].Value = genre;
                    sqlAdapterVinyl.SelectCommand.Parameters["@Price"].Value = price;
                    sqlAdapterVinyl.SelectCommand.Parameters["@IdVinyl"].Value = idVinyl;

                    sqlAdapterVinyl.SelectCommand.ExecuteNonQuery();


                    int idCrate = Int32.Parse(Convert.ToString(selectedRow.Cells["IdCrate"].Value));
                    sqlAdapterVinyl.SelectCommand = new SqlCommand("SELECT * FROM Vinyl WHERE IdCrate = @IdCrate", sqlConnection);
                    sqlAdapterVinyl.SelectCommand.Parameters.Add("@IdCrate", SqlDbType.Int);
                    sqlAdapterVinyl.SelectCommand.Parameters["@IdCrate"].Value = idCrate;

                    dataSet.Clear();
                    sqlAdapterVinyl.Fill(dataSet,"Vinyl");
                    vinylView.DataSource = dataSet.Tables[0];

                    sqlConnection.Close();

                }
            }
            catch (Exception)
            {
                Console.WriteLine("Eroare update button");
            }
        }
    }
}
