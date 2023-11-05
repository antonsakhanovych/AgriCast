import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import React, { useState, useEffect } from 'react';
import './LeafletMap.css';
import location from './location.png';

function LeafletMap({ selectedDate, buttonClicked, setDataToConsole }) {
  const [currentLocation, setCurrentLocation] = useState(null);
  const [markerPosition, setMarkerPosition] = useState(null);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition((position) => {
      const { latitude, longitude } = position.coords;
      const initialLocation = { lat: latitude, lng: longitude };
      setCurrentLocation(initialLocation);
      setMarkerPosition(initialLocation);
    }, (error) => {
      console.error("Error getting location:", error);
    });
  }, []);

  const handleMapClick = (e) => {
    const { lat, lng } = e.latlng;
    setMarkerPosition({ lat, lng });

    // Проверьте, была ли нажата кнопка, перед выводом информации в консоль

      // Создайте объект с координатами и датой
      const dataToConsole = {
        date: selectedDate,
        coordinates: { lat, lng },
      };

      // Обновите состояние, чтобы отобразить данные в компоненте App
      setDataToConsole(dataToConsole);

    
  };

  return (
    <div className='centralDiv'>
      <MapContainer
        center={currentLocation || [0, 0]}
        zoom={13}
        className="map-container"
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {currentLocation && markerPosition && (
          <Marker position={markerPosition}
            icon={L.icon({
              iconUrl: location,
              iconSize: [32, 32],
              iconAnchor: [16, 32],
            })}
          >
            <Popup>
              <div className="popup-content">
                Current Location:<br />
                Latitude: {markerPosition.lat}<br />
                Longitude: {markerPosition.lng}
              </div>
            </Popup>
          </Marker>
        )}
        <MapClickHandler onMapClick={handleMapClick} />
      </MapContainer>
    </div>
  );
}

function MapCenter({ currentLocation }) {
    return null;
}

function MapClickHandler({ onMapClick }) {
    const map = useMapEvents({
        click: onMapClick,
    });
    return null;
}

export default LeafletMap;
