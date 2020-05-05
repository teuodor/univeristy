using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Laborator1.Domain.Entities;

namespace Laborator1.Domain.Validator
{
    public class CrateValidator : IValidator<Crate>
    {
        public void Validate(Crate entity)
        {
            var errors = "";
            if(entity.Id < 0)
            {
                errors += "Crate id must be a positive integer!!! \n";
            }
            if(entity.IdVinyl < 0)
            {
                errors += "Crate id vinyl must be a positive integer!!! \n";
            }
            if (!(errors.Equals("")))
            {
                throw new ValidatorException(errors);
            }
        }
    }
}
