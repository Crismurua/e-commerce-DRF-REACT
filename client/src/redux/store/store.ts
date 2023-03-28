import { configureStore } from "@reduxjs/toolkit";
import productSlice from "../states/products";
import { Category, City, Discount, Product, Size, State, User } from "@/models";
import cartSlice from "../states/cart";

export interface AppStore {
    // users: User[];
    products: Product[];
    cart: Product[];
    // categories: Category[];
    // sizes: Size[];
    // discounts: Discount[];
    // states: State[];
    // cities: City[];
}

const store = configureStore<AppStore>({
    reducer: {
        products: productSlice.reducer,
        cart: cartSlice.reducer, 
    }
})

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
