import React, { useEffect } from 'react';
import L, { LatLng, GeoJSON } from 'leaflet';
import { useLeaflet } from 'react-leaflet';
import LoadingSpinner from '../loadingSpinner';
import { geojsonMarkerOptions } from '../marker';
import { DriverProps } from '../../types/DriverProps';
import { useDriverFetcher } from '../hooks/useDriverFetcher';
import { onEachFeature } from './helpers';
// import styles from './index.module.sass';

let geojson: GeoJSON;

const DriverMap: React.FC = () => {
    const { drivers, loading, error } = useDriverFetcher();
    const { map } = useLeaflet();

    useEffect(() => {
        if (map && map.hasLayer(geojson)) map.removeLayer(geojson);
        geojson = L.geoJSON(drivers.features, {
            onEachFeature,
            pointToLayer: (feature: DriverProps, latlng: LatLng) => {
                const driverNum = feature.id;
                
                return L.circleMarker(latlng, geojsonMarkerOptions(driverNum));
            }
        });

        if (map) geojson.addTo(map);
    }, [drivers, error, map]);

    if (loading) return <LoadingSpinner />;
    return null;
};

export default DriverMap;
