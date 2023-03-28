import { LocalStorageTypes, Product } from "@/models";
import { getLocalStorage, setLocalStorage } from "@/utils";
import { createSlice } from "@reduxjs/toolkit";

const initialState : Product[] = [];

const initialStateTest = () => {
    const localStorageData = getLocalStorage(LocalStorageTypes.CART)
    ? JSON.parse(getLocalStorage(LocalStorageTypes.CART) as string)
    : initialState;

    return localStorageData;
}

export const cartSlice = createSlice({
    name: 'cart',
    initialState: initialStateTest(),
    reducers: {
        addProduct: (state, action) => {
            setLocalStorage(LocalStorageTypes.CART, action.payload);
            return action.payload
        },
        removeProduct: (state, action) => {
            const filterState = state.filter((p : Product) => p.id !== action.payload.id)
            setLocalStorage(LocalStorageTypes.CART, filterState);
            return filterState;
        }
    }
})

export const {  addProduct, removeProduct } = cartSlice.actions;

export default cartSlice;
