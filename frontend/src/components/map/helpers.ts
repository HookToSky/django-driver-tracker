import { Layer } from 'leaflet';
import { DriverProps } from '../../types/DriverProps';

export const onEachFeature = (feature: DriverProps, layer: Layer) => {
    const {
        properties: { driverName, driverCityOrigin, driverLanguage, driverPhone, driverInfo, licensePlate},
        geometry: { coordinates }
    } = feature;

    const content = `
      <div data-testid="popup">
      <h3 style="font-size: 1.17em; font-weight: bold">${driverName}</h3>
      <b>Nationality</b>: ${driverCityOrigin} <br>
      <b>Language</b>: ${driverLanguage} <br>
      <b>Lon</b>: ${coordinates[0]} <br>
      <b>Lat</b>: ${coordinates[1]} <br>
      <b>Phone</b>: ${driverPhone} km <br>
      <b>Info</b>: ${driverInfo} Richter <br>
      <b>License Plate</b>: ${licensePlate} <br>
      </div>
    `;

    layer.bindPopup(content);
};
