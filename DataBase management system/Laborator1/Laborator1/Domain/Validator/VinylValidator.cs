using Laborator1.Domain.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Laborator1.Domain.Validator
{
    public class VinylValidator : IValidator<Vinyl>
    {
        public void Validate(Vinyl entity)
        {
            var errors = "";
            if(entity.Id < 0)
            {
                errors += "Vinyl id must be a positive integer!!! \n";
            }
            if(entity.Name.Length > 50 || entity.Name.Length == 0)
            {
                errors += "Vinyl name must have a length between 0 and 50!!! \n";
            }
            if(entity.Genre.Length > 50 || entity.Genre.Length == 0)
            {
                errors += "Vinyl genre name must have a length between 0 and 50!!! \n"; 
            }
            if(entity.Price < 0)
            {
                errors += "Vinyl price must be a positive integer!!! \n";
            }
            if(entity.IdCrate < 0)
            {
                errors += "Vinyl id crate must be a positive number!!! \n";
            }

            if (!(errors.Equals("")))
            {
                throw new ValidatorException(errors);
            }
        }
    }
}
