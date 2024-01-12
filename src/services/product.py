from src.model.product import Product
from datetime import datetime


class ProductService:
    """all product services"""

    def create_product_service(self, db, product_data, current_user):
        """create product service"""

        product = Product(**product_data.dict())
        product.user_id = current_user
        db.add(product)
        db.commit()

        return product

    def get_product_service(self, db, product_id):
        """get product service"""

        product = (
            db.query(Product)
            .filter(
                Product.id == product_id,
                Product.is_deleted == False,
            )
            .first()
        )
        return product

    def get_user_all_product_service(self, db, user_id):
        """get particular user all products API"""

        product = (
            db.query(Product)
            .filter(
                Product.user_id == user_id,
                Product.is_deleted == False,
            )
            .all()
        )

        return product

    def update_product_service(self, db, product_id, product_data, current_user):
        """update product services"""

        product = (
            db.query(Product)
            .filter(
                Product.id == product_id,
                Product.is_deleted == False,
            )
            .first()
        )

        for field, value in product_data.dict(exclude_unset=True).items():
            setattr(product, field, value)

        product.updated_at = datetime.utcnow()
        product.updated_by = current_user
        db.commit()

        return {"message": f"successfully updated {product_id} product"}

    def delete_product_service(self, db, product_id, current_user):
        """delete product services"""

        product = (
            db.query(Product)
            .filter(
                Product.id == product_id,
                Product.is_deleted == False,
            )
            .first()
        )

        product.is_deleted = True
        product.deleted_at = datetime.utcnow()
        product.deleted_by = current_user
        db.commit()

        return {"message": f"Successfully deleted {product_id}"}
