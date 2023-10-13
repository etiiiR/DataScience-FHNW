from surrealdb import Surreal

async def main():
    """Example of how to use the SurrealDB client."""
    async with Surreal("ws://185.232.68.247:8111/rpc") as db:
        await db.signin({"user": "Etiiir", "pass": "Welcome12"})
        await db.use('cml1', 'index')
        # set the name space
        await db.create('person', {'name': 'Etiiir', 'age': 20})
        await db.create('person', {'name': 'Dirk', 'age': 25})
        await db.create('person', {'name': 'Manu', 'age': 30})
        await db.create('person', {'name': 'Lumen', 'age': 35})
        await db.create('person', {'name': 'Didi', 'age': 40})
        await db.create('person', {'name': 'Lukas', 'age': 45})
        await db.create('person', {'name': 'Lukas', 'age': 50})
        await db.create('person', {'name': 'Lukas', 'age': 55})
        await db.create('person', {'name': 'Lukas', 'age': 60})
        await db.create('person', {'name': 'Lukas', 'age': 65})
        # create new sklearn model and train it with the data farm and save the model as .surml

        persons = await db.query('SELECT * FROM person')
        print(await db.query('INFO FOR NS;'))
        # Get all persons
        #persons = await db.select('person')
        #print(persons)



if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
    