using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Laborator1.Domain.Entities;
using Laborator1.Domain.Validator;

namespace Laborator1.Repository
{
    public delegate SqlCommand InsCmd<E>(E entity, SqlConnection conn);
    public delegate SqlCommand DelCmd<E>(E entity, SqlConnection conn);
    public delegate SqlCommand UpdCmd<E>(E entity, SqlConnection conn);
    public delegate SqlCommand FindCmd<Id>(Id id, SqlConnection conn);

    public abstract class AbstractCRUDRepository<Id, E> : IRepository<Id, E> where E : class, IHaveID<Id>
    {
        protected readonly IValidator<E> _validator;
        protected readonly string _connString;
        protected readonly InsCmd<E> _insCmd;
        protected readonly DelCmd<E> _delCmd;
        protected readonly UpdCmd<E> _updCmd;
        protected readonly FindCmd<Id> _findCmd;


        public AbstractCRUDRepository(IValidator<E> validator, string connString, InsCmd<E> insCmd,
            DelCmd<E> delCmd, UpdCmd<E> updCmd, FindCmd<Id> findCmd)
        {
            _validator = validator;
            _connString = connString;
            _insCmd = insCmd;
            _delCmd = delCmd;
            _updCmd = updCmd;
            _findCmd = findCmd;
            SqlConnection sqlConnection = new SqlConnection(_connString);
            try
            {
                sqlConnection.Open();
                sqlConnection.Close();
            }
            catch (Exception)
            {
                throw new ValidatorException("Could not establish the connection!");
            }
        }

        public bool FindOne(Id id)
        {
            if(id == null)
            {
                throw new IllegalArgumentException("Entity id can't be null!!!");
            }

            using(SqlConnection sqlConn = new SqlConnection(this._connString))
            {
                var cmd = _findCmd(id, sqlConn);
                int result = cmd.ExecuteNonQuery();
                return result > 0 ? true : false;
            }
        }

        public IEnumerable<E> FindAll()
        {
            return null;
        }

        public E Save(E entity)
        {
            if(entity == null)
            {
                throw new IllegalArgumentException("Entity can't be null!");
            }
            if (FindOne(entity.Id))
            {
                return entity;
            }
            _validator.Validate(entity);
            using(SqlConnection sqlConn = new SqlConnection(this._connString))
            {
                var cmd = _insCmd(entity, sqlConn);
                int rowsAffected = cmd.ExecuteNonQuery();
                sqlConn.Close();

                if(rowsAffected != 0)
                {
                    return null;
                }

                return entity;
            }
        }

        public E Delete(Id id)
        {
            if(id == null)
            {
                throw new IllegalArgumentException("Entity can't be null!");
            }

            return null;
        }

        public E Update(E entity)
        {
            return null;
        }
    }
}
