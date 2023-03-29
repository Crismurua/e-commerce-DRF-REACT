import { Product } from "./product";
import { User } from "./user";

export interface Rating{
    user: User;
    product: Product;
    starts: number;
    review: string;
}
