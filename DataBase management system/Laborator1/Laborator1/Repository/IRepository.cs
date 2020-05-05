using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Laborator1.Repository
{
    interface IRepository<Id, E>
    {
        E FindOne(Id id);

        IEnumerable<E> FindAll();

        void Save(E entity);

        void Delete(Id id);

        void Update(E entity);

    }
}
