from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from Models.Models import User, Product, CartItem
from config import settings

app = FastAPI()

engine = create_async_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Зависимость для получения сессии БД
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/cart/{user_id}/add")
async def add_to_cart(user_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):

    cart_item = await db.execute(select(CartItem).where(CartItem.user_id == user_id, CartItem.product_id == product_id))
    cart_item = cart_item.scalars().first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
        db.add(cart_item)

    await db.commit()
    return {"status": "success"}

@app.post("/cart/{user_id}/remove")
async def remove_from_cart(user_id: int, product_id: int, db: Session = Depends(get_db)):
    
    cart_item = await db.execute(select(CartItem).where(CartItem.user_id == user_id, CartItem.product_id == product_id))
    cart_item = cart_item.scalars().first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Item not found in cart")

    await db.delete(cart_item)
    await db.commit()
    return {"status": "success"}

@app.post("/cart/{user_id}/update")
async def update_cart_item(user_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):

    cart_item = await db.execute(select(CartItem).where(CartItem.user_id == user_id, CartItem.product_id == product_id))
    cart_item = cart_item.scalars().first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Item not found in cart")

    cart_item.quantity = quantity
    await db.commit()
    return {"status": "success"}
