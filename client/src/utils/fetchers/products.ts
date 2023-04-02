import { Product, Category, Size, Rating, Discount } from "@/models";
import { createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import { BACKEND_DIR } from "@/main";

interface UpdateProductPayload {
    id: string;
    productData: Partial<Product>;
  }

export const getProducts = createAsyncThunk(
    "products/getProducts",
    async (data, thunkApi) => {
        try{
            const response = await axios.get<Product[]>(BACKEND_DIR + "products/products", {
                method: 'GET',
                headers: {"Content-type": "application/json; charset=UTF-8"},
            });
            return response.data;

        } catch(err : any) {
            return thunkApi.rejectWithValue(err.message)
        }
    }
)

export const findProduct = createAsyncThunk(
    "products/findProduct",
    async (id : string, thunkApi) => {
        try{
            const response = await axios.get<Product>(BACKEND_DIR + `products/products/${id}`, {
                method: 'GET',
                headers: {"Content-type": "application/json; charset=UTF-8"},
            });
            return response.data;

        } catch(err : any) {
            return thunkApi.rejectWithValue(err.message)
        }
    }
)

export const createProduct = createAsyncThunk(
    "products/createProduct",
    async (productData : Partial<Product>, thunkApi) => {
        try{
            const response = await axios.post<Product>(BACKEND_DIR + `products/products`, productData, {
                method: 'POST',
                headers: {"Content-type": "application/json; charset=UTF-8"},
            });
            return response.data;

        } catch(err : any) {
            return thunkApi.rejectWithValue(err.message)
        }
    }
)

export const updateProduct = createAsyncThunk(
    "products/updateProduct",
    async ({id, productData} : UpdateProductPayload, thunkApi) => {
        try{
            const response = await axios.put<Product>(BACKEND_DIR + `products/products/${id}`, productData, {
                method: 'PUT',
                headers: {"Content-type": "application/json; charset=UTF-8"},
            });
            return response.data;

        } catch(err : any) {
            return thunkApi.rejectWithValue(err.message)
        }
    }
)

export const deleteProduct = createAsyncThunk(
    "products/deleteProduct",
    async (id : string, thunkApi) => {
        try{
            const response = await axios.delete(BACKEND_DIR + `products/products/${id}`, {
                method: 'DELETE',
                headers: {"Content-type": "application/json; charset=UTF-8"},
            });
            return response.data;

        } catch(err : any) {
            return thunkApi.rejectWithValue(err.message)
        }
    }
)

export const getCategories = createAsyncThunk(
    "categories/getCategories",
    async (data, thunkApi) => {
        try{
            const response = await axios.get<Category[]>(
                BACKEND_DIR + "products/categories", {
                    method: 'GET',
                    headers: {"Content-type": "application/json; charset=UTF-8"},
                }
            );
            return response.data;

        } catch(err : any) {
            return thunkApi.rejectWithValue(err.message)
        }
    }
)

export const getSizes = createAsyncThunk(
    "sizes/getSizes",
    async (data, thunkApi) => {
        try{
            const response = await axios.get<Size[]>(
                BACKEND_DIR + "products/sizes", {
                    method: 'GET',
                    headers: {"Content-type": "application/json; charset=UTF-8"},
                }
            );
            return response.data;

        } catch(err : any){
            return thunkApi.rejectWithValue(err.message)
        }
    }
)

export const getRatings = createAsyncThunk(
    "ratings/getRatings",
    async (data, thunkApi) => {
        try{
            const response = await axios.get<Rating[]>(
                BACKEND_DIR + "products/ratings", {
                    method: 'GET',
                    headers: {"Content-type": "application/json; charset=UTF-8"},
                }
            );
            return response.data
        } catch(err : any){
            return thunkApi.rejectWithValue(err.message)
        }
    }
)
