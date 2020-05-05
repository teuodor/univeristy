using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Laborator1.Domain.Entities
{
    public class Vinyl : IHaveID<int>
    {
        public Vinyl(int id, string name, string genre, int price, int idCrate)
        {
            Id = id;
            Name = name;
            Genre = genre;
            Price = price;
            IdCrate = idCrate;
        }

        public int Id { get; set; }
        
        public string Name { get; set; }
        
        public string Genre { get; set; }
        
        public int Price { get; set; }

        public int IdCrate { get; set; }

        public override bool Equals(object obj)
        {
            if(!(obj is Vinyl))
            {
                return false;
            }

            var vinyl = (Vinyl)obj;

            return vinyl.Id.Equals(this.Id);
        }

        public override int GetHashCode()
        {
            return Id.GetHashCode() + Name.GetHashCode();
        }
    }
}
