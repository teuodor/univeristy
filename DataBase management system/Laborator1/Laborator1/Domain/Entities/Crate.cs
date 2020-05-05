using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Laborator1.Domain.Entities
{
    public class Crate : IHaveID<int>
    {
        public Crate(int id, int idVinyl)
        {
            Id = id;
            IdVinyl = idVinyl;
        }

        public int Id { get; set; }
        public int IdVinyl { get; set; }

        public override bool Equals(object obj)
        {
            if(!(obj is Crate))
            {
                return false;
            }

            var crate = (Crate)obj;

            return crate.Id.Equals(this.Id);
        }

        public override int GetHashCode()
        {
            return (Id.GetHashCode() + 2) * (IdVinyl.GetHashCode() + 3);
        }
    }
}
