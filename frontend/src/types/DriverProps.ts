export interface DriverProps {
    geometry: any;
    id?: number | string;
    properties: {
        driverName: string;
        driverCityOrigin: string;
        driverLanguage: string;
        driverPhone: string;
        driverInfo: string;
        licensePlate: string;
        kmDriven: number;
    };
}
