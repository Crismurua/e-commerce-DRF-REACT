import { LocalStorageTypes, Product } from "@/models";
import { createProduct, deleteProduct, getLocalStorage, setLocalStorage, updateProduct } from "@/utils";
import { getProducts } from "@/utils";
import { createSlice } from "@reduxjs/toolkit";

const initialState : Product[] = [];

export const productSlice = createSlice({
    name: 'products',
    initialState: getLocalStorage(LocalStorageTypes.PRODUCTS) ? JSON.parse(getLocalStorage(LocalStorageTypes.PRODUCTS) as string) : initialState,
    reducers: {
        setProducts(state, action) {
            return action.payload;
          },
    },
    extraReducers(builder) {
        builder
        .addCase(getProducts.fulfilled, (state, action) => {
            setLocalStorage(LocalStorageTypes.PRODUCTS, state)
            return action.payload
        })
        .addCase(createProduct.fulfilled, (state, action) => {
            state.products.push(action.payload);
          })
        .addCase(updateProduct.fulfilled, (state, action) => {
            const index = state.products.findIndex((product : Product) => product.id === action.payload.id);
            state.products[index] = action.payload;
          })
        .addCase(deleteProduct.fulfilled, (state, action) => {
            state.products = state.products.filter((product : Product) => product.id !== action.payload);
          });
    }
})

export default productSlice;
