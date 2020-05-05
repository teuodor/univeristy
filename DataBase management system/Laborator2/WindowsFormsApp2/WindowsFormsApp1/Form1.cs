using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        private string parentTableName;
        private string childTableName;
        private string foreignKeyName;
        private string idName;
        private string connectionString;
        private SqlConnection _sqlConnection;
        private SqlDataAdapter _dataAdapterParent = new SqlDataAdapter();
        private SqlDataAdapter _dataAdapterChild = new SqlDataAdapter();
        private DataSet _dataSet = new DataSet();
        private string selectParent; 
        
        public Form1()
        {
            InitializeComponent();
            parentTableName = ConfigurationManager.AppSettings["parentTableName"];
            childTableName = ConfigurationManager.AppSettings["childTableName"];
            foreignKeyName = ConfigurationManager.AppSettings["foreignKeyName"];
            connectionString = "Data Source=DESKTOP-SIFAM82;Initial Catalog=VinylSqlShop;Integrated Security=True";
            _sqlConnection = new SqlConnection(connectionString);
            selectParent = "SELECT * FROM " + parentTableName;
            _sqlConnection.Open();
            loadParent();
            _sqlConnection.Close();
        }

        private void loadParent()
        {
            _dataAdapterParent.SelectCommand = new SqlCommand(selectParent, _sqlConnection);
            _dataAdapterParent.Fill(_dataSet, "Parent");
            parentView.DataSource = _dataSet.Tables["Parent"];
        }
        
        private void closeButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            if (_dataSet.Tables.Count == 1)
            {
                MessageBox.Show("Choose a parent ID");
                return;
            }

            try
            {
                var commandBuilder = new SqlCommandBuilder(_dataAdapterChild);
                _dataAdapterChild.UpdateCommand = commandBuilder.GetUpdateCommand();
                _dataAdapterChild.DeleteCommand = commandBuilder.GetDeleteCommand();
                _dataAdapterChild.InsertCommand = commandBuilder.GetInsertCommand();
                _dataAdapterChild.Update(_dataSet, "Child");
                MessageBox.Show("Synchronized");
            }
            catch (Exception)
            { 
                Console.WriteLine("Error updateButton");
            }
        }
        
        private void crateView_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            try
            {
                parentView.CurrentRow.Selected = true;
                var id = parentView.Rows[e.RowIndex].Cells[idName].FormattedValue.ToString();
                _sqlConnection.Open();
                _dataAdapterChild.SelectCommand = new SqlCommand("SELECT * FROM " + childTableName + " WHERE " + foreignKeyName +" = @IDChild", _sqlConnection);
                _dataAdapterChild.SelectCommand.Parameters.AddWithValue("@IDChild", id);

                _dataSet.Clear();
                loadParent();
                _dataAdapterChild.Fill(_dataSet, "Child");
                childView.DataSource = _dataSet.Tables["Child"];
                _sqlConnection.Close();
            }
            catch(Exception)
            {
                Console.WriteLine("Error CellClick View");
            }
        }

        private void deleteButton_Click(object sender, EventArgs e)
        {
            try
            {
                _sqlConnection.Open();
                _dataAdapterChild.SelectCommand = new SqlCommand("DELETE FROM " + childTableName + " WHERE ID = @IDChild",_sqlConnection);
                if(childView.SelectedCells.Count > 0)
                {
                    int selectedRowIndex = childView.SelectedCells[0].RowIndex;
                    DataGridViewRow selectedRow = childView.Rows[selectedRowIndex];
                    var id = Convert.ToString(selectedRow.Cells[idName].Value);

                    _dataAdapterChild.SelectCommand.Parameters.AddWithValue("@IDChild", id);

                    _dataAdapterChild.SelectCommand.ExecuteNonQuery();

                    _sqlConnection.Close();
                }
                else
                {
                    _sqlConnection.Close();
                    throw new Exception();
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Eroare Button delete");
            }
        }
    }
}