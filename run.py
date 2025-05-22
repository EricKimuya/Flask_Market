from market import app, db
from market.models import Item

with app.app_context():
    db.create_all()  # Ensure tables are created

    # Add initial data if the table is empty
    if not Item.query.first():
        item1 = Item(name="Phone", price=500, barcode="893212299897", description="A smartphone")
        item2 = Item(name="Laptop", price=900, barcode="123985473165", description="A powerful laptop")
        db.session.add_all([item1, item2])
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
