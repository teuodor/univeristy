using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Laborator1.Domain.Entities
{
    public interface IHaveID<ID>
    {
        ID Id { get; set; }
    }
}
