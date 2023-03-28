import { LocalStorageTypes, Product } from "@/models";
import { getLocalStorage, setLocalStorage } from "@/utils/localstorage.util";
import { getProducts } from "@/utils/fetchers";
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
        builder.addCase(getProducts.fulfilled, (state, action) => {
            setLocalStorage(LocalStorageTypes.PRODUCTS, state)
            return action.payload
        })
    }
})

export default productSlice;
