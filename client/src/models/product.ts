import { Category } from "./category";
import { Size } from "./size";

export interface Product{
    id: string;
    name: string;
    description: string;
    image: string;
    price: number;
    stock: number;
    size: Size;
    category: Category;
};
