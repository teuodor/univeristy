using Laborator1.Domain.Entities;
using Laborator1.Domain.Validator;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;

namespace Laborator1.Repository
{
    public class CrateDBRepository : AbstractCRUDRepository<int, Crate>
    {
        public CrateDBRepository(IValidator<Crate> val, string connString):
            base(val, connString, insCmd, delCmd, updCmd, findCmd)
        {

        }

        private static SqlCommand insCmd(Crate crate, SqlConnection sqlConnection)
        {
            SqlCommand cmd = new SqlCommand("INSERT INTO Crate" + "(IdCrate, IdVinyl)" +
                "VALUES(@IdCrate, @IdVinyl)", sqlConnection);

            cmd.Parameters.Add("@IdCrate", SqlDbType.Int);
            cmd.Parameters.Add("@IdVinyl", SqlDbType.Int);

            cmd.Parameters["@IdCrate"].Value = crate.Id;
            cmd.Parameters["@IdVinyl"].Value = crate.IdVinyl;

            return cmd;
        }

        public static SqlCommand findCmd(int id, SqlConnection sqlConnection)
        {
            SqlCommand cmd = new SqlCommand("SELECT * FROM Crate");
            return cmd;

        }

        public static SqlCommand delCmd(Crate crate, SqlConnection sqlConnection)
        {
            return null;
        }

        public static SqlCommand updCmd(Crate crate, SqlConnection sqlConnection)
        {
            return null;
        }

        
    }
}
