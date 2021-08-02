import React, { FC } from 'react';
import { Map, TileLayer, LayersControl, ScaleControl } from 'react-leaflet';
import EarthquakeMap from '../map';
import { tileLayerOptions } from '../../constants/tileLayerOptions';
import styles from './index.module.sass';
import { TileProps } from '../../types/TileProps';

const MapContainer: FC = () => {
    return (
        <div data-testid="map-container">
            <Map center={[0, 0]} zoom={3} className={styles.map}>
                <LayersControl position="topright">
                    {tileLayerOptions.map(
                        ({
                            id,
                            name,
                            attribution,
                            url,
                            checked
                        }: TileProps) => (
                            <LayersControl.BaseLayer
                                key={id}
                                name={name}
                                checked={checked}>
                                <TileLayer
                                    attribution={attribution}
                                    url={url}
                                />
                            </LayersControl.BaseLayer>
                        )
                    )}
                </LayersControl>
                <EarthquakeMap />
                <ScaleControl />
            </Map>
        </div>
    );
};

export default MapContainer;
