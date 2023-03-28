import { State } from "./state";
import { City } from "./city";

export interface User {
    id: string;
    username: string;
    email: string;
    first_name: string;
    last_name: string;
    image: string;
    phone: string;
    state: State;
    city: City;
};
