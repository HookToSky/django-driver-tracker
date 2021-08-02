import { useState, useEffect } from 'react';
import { getDrivers } from '../../services/driverService';

export function useDriverFetcher(): any {
    const [drivers, setDrivers] = useState({});
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);
    const fetchEarthquakes = async () => {
        try {
            const data = await getDrivers();
            setDrivers(data);
        } catch (err) {
            setError(true);
        }
        setLoading(false);
    };
    useEffect(() => {
        setLoading(true);
        setError(false);
        fetchEarthquakes();
    }, []);

    return { drivers, loading, error };
}
