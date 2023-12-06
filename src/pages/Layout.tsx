import { Link, Outlet } from "react-router-dom";
import { Header } from "./Header";



function Layout(): JSX.Element {
    return (
        <div>
            <Header />



            <hr />


            <Outlet />
        </div>
    );
}

export { Layout };